using MailKit.Net.Smtp;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Identity.UI.Services;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;
using MimeKit;
using Services.Entities;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Services
{
    public class EmailSender: IEmailSender
    {
        private readonly SmtpSettings _smtpSettings;
        private readonly IWebHostEnvironment _env;
        private readonly ILogger<EmailSender> _logger;
        
        public EmailSender(IOptions<SmtpSettings> smtpSettings, IWebHostEnvironment env, ILogger<EmailSender> logger)
        {
            _smtpSettings = smtpSettings.Value;
            _env = env;
            _logger = logger;
        }
        public async Task SendEmailAsync(string email, string subject, string body)
        {
            try
            {
                var message = new MimeMessage();
                message.From.Add(new MailboxAddress(_smtpSettings.SenderName, _smtpSettings.SenderEmail));
                message.To.Add(new MailboxAddress(email));
                message.Subject = subject;
                message.Body = new TextPart("html")
                {
                    Text = body
                };

                using (var client = new SmtpClient())
                {
                    client.ServerCertificateValidationCallback = (s, c, h, e) => true;

                    if (_env.IsDevelopment())
                    {
                        await client.ConnectAsync(_smtpSettings.MailServer, _smtpSettings.MailPort, false);
                    }
                    else
                    {
                        await client.ConnectAsync(_smtpSettings.MailServer);
                    }
                    await client.AuthenticateAsync(_smtpSettings.Username, _smtpSettings.Password);
                    await client.SendAsync(message);
                    await client.DisconnectAsync(true);
                    _logger.LogInformation("EmailService: OK/ Message send!");
                }
            }
            catch(Exception e)
            {
                _logger.LogError($"EmailService: {e.Message}!");
                throw new InvalidOperationException(e.Message);
            }
        }
    }
}
