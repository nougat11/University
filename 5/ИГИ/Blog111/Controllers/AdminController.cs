using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Blog111.BusinessManager.Interfaces;
using Blog111.Models.AdminViewModels;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace Blog111.Controllers
{
    
    public class AdminController : Controller
    {
        private readonly IAdminBusinessManager adminBusinessManager;
        private ILogger<AdminController> logger;
        public AdminController(IAdminBusinessManager adminBusinessManager, ILogger<AdminController> logger)
        {
            this.adminBusinessManager = adminBusinessManager;
            this.logger = logger;
        }
        public async Task<IActionResult> Index()
        {
            logger.LogInformation("AdminController: Index OK ");
            return View(await adminBusinessManager.GetAdminDashboard(User));
        }
        public async Task<IActionResult> About()
        {
            logger.LogInformation("AdminController: About OK ");
            return View(await adminBusinessManager.GetAboutViewModel(User));
        }
        [HttpPost]
        public async Task<IActionResult> UpdateAbout(AboutViewModel aboutViewModel)
        {
            await adminBusinessManager.UpdateAbout(aboutViewModel, User);
            logger.LogInformation("AdminController: UpdateAbout OK ");
            return RedirectToAction("About");
        }
    }
}
