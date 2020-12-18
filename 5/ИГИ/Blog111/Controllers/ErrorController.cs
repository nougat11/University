using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Blog111.Models;
using Microsoft.AspNetCore.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace Blog111.Controllers
{
    public class ErrorController : Controller
    {
        private readonly ILogger<ErrorController> logger;

        public ErrorController(ILogger<ErrorController> logger)
        {
            this.logger = logger;
        }
        [Route("Error/{statuscode}")]
        public IActionResult Error(int statuscode)
        {
            
            logger.LogError($"Error {statuscode}");
            ViewBag.statuscode = statuscode;
            return View();
        }
        [Route("Exception")]
        public IActionResult Exception()
        {
            var exeptionDetails = HttpContext.Features.Get<IExceptionHandlerPathFeature>();
            logger.LogError($"{exeptionDetails.Error.Message}");
            return View();
        }

    }
}
