using Blog111.Entities;
using Microsoft.AspNetCore.Http;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Blog111.Models.AdminViewModels
{
    public class AboutViewModel
    {
        public User user { get; set; }
        [Display(Name = "Header Image")]
        public IFormFile HeaderImage { get; set; }
        [Display(Name = "Header")]
        public string Header { get; set; }
        public string Content { get; set; }
    }
}
