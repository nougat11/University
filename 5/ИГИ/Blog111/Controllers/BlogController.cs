using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Blog111.BusinessManager.Interfaces;
using Blog111.Data;
using Blog111.Models.BlogViewModels;
using Entities;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.Extensions.Logging;
using Services.Interfaces;

namespace Blog111.Controllers
{
    
    public class BlogController : Controller
    {
        private readonly IPostBusinessManager postBusinessManager;
        private readonly IPostService postService;
        private readonly ApplicationDbContext applicationDbContext;
        private readonly ILogger<BlogController> logger;
        public BlogController(IPostBusinessManager postBusinessManager, IPostService postService, ApplicationDbContext applicationDbContext, ILogger<BlogController> logger)
        {
            this.postBusinessManager = postBusinessManager;
            this.postService = postService;
            this.applicationDbContext = applicationDbContext;
            this.logger = logger;
        }
        [Route("Post/{id}"), AllowAnonymous]
        public async Task<IActionResult> Index(int? id)
        {
            
            var actionResult = await postBusinessManager.GetPostViewModel(id, User);

            if (actionResult.Result is null)
            {
                return View(actionResult.Value);
            }
            logger.LogInformation("PostController: GetPostView model OK.");
            return actionResult.Result;
        }

        public IActionResult Create()
        {
            CreateViewModel Model = new CreateViewModel();
            var cat = applicationDbContext.Categories;
            List < Category > categories= cat.ToList();
            Model.Categories = new List<SelectListItem>();
            foreach (Category category in categories)
            {
                Model.Categories.Add(new SelectListItem { Value = category.Title, Text = category.Title });
            }
            logger.LogInformation("PostController: CreateView model OK.");
            return View(Model);

        }
        [Authorize(Roles = "Admin")]
        public IActionResult CreateCategory()
        {
            logger.LogInformation("PostController: CreateCategory model OK.");
            return View(new CreateCategoryViewModel());
        }

        [HttpPost]
        public async Task <IActionResult> Add(CreateViewModel createBlogViewModel)
        {
            await postBusinessManager.CreatePost(createBlogViewModel, User);
            logger.LogInformation("PostController: Create model OK.");
            return RedirectToAction("Create");
        }


        [HttpPost]
        public async Task<IActionResult> AddCategory(CreateCategoryViewModel createCategoryViewModel)
        {
            await postBusinessManager.CreateCategory(createCategoryViewModel, User);
            logger.LogInformation("PostController: AddCategory model OK.");
            return RedirectToAction("CreateCategory");
        }

        [HttpPost]
        public async Task<IActionResult> Update(EditViewModel editViewModel)
        {
            var actionResult = await postBusinessManager.UpdatePost(editViewModel, User);
            if (actionResult.Result is null)
                return RedirectToAction("Edit", new { editViewModel.Post.ID });
            logger.LogInformation("PostController: Update method OK.");
            return actionResult.Result;
        }
        [HttpPost]
        public async Task<IActionResult> Comment(PostViewModel postViewModel)
        {
            var actionResult = await postBusinessManager.CreateComment(postViewModel, User);
            if (actionResult.Result is null)
            {
                return RedirectToAction("Index", new { postViewModel.Post.ID });
            }
            logger.LogInformation("PostController: Comment method OK.");
            return actionResult.Result;
        }

        public async Task<IActionResult> Edit(int? id)
        {
            var actionResult = await postBusinessManager.GetEditViewModel(id, User);

            if (actionResult.Result is null)
            {
                return View(actionResult.Value);
            }
            logger.LogInformation("PostController: Edit method OK.");

            return actionResult.Result;
        }
    }
}
