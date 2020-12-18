using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Blog111.Models;
using Blog111.BusinessManager.Interfaces;
using Services.Interfaces;
using Entities;

namespace Blog111.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly IPostBusinessManager blogBusinessManager;
        private readonly IHomeBusinessManager homeBusinessManager;
        private readonly IPostService postService;

        public HomeController(ILogger<HomeController> logger, IPostBusinessManager blogBusinessManager, IHomeBusinessManager homeBusinessManager, IPostService postService)
        {
            _logger = logger;
            this.blogBusinessManager = blogBusinessManager;
            this.homeBusinessManager = homeBusinessManager;
            this.postService = postService;

        }

        public IActionResult Index(string searchString, int? page)
        {
            _logger.LogInformation("HomeController: Index OK");
            return View(blogBusinessManager.GetIndexViewModel(searchString, page));
        }

        public IActionResult Author(string authorid, string searchstring, int? page)
        {
            var actionResult = homeBusinessManager.GetAuthorViewModel(authorid, searchstring, page);
            if (actionResult.Result is null)
            {
                return View(actionResult.Value);
            }
            _logger.LogInformation("HomeController: Author OK");

            return actionResult.Result;
        }

        public IActionResult Category(int id, string searchstring, int? page)
        {
            var actionResult = homeBusinessManager.GetCategoryViewModel(id, searchstring, page);
            if (actionResult.Result is null)
            {
                return View(actionResult.Value);
            }
            _logger.LogInformation("HomeController: Category OK");
            return actionResult.Result;
        }
        public IActionResult IndexCategories()
        {
            List<Category> categories = postService.GetCategories();
            return View(categories);
        }

    }
}
