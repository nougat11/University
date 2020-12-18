using Blog111.BusinessManager.Interfaces;
using Blog111.Models.HomeViewModels;
using Entities;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using PagedList.Core;
using Services.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Blog111.BusinessManager
{
    public class HomeBusinessManager:IHomeBusinessManager
    {
        private readonly IPostService postService;
        private readonly IUserService userService;
        private ILogger<HomeBusinessManager> logger;

        public HomeBusinessManager(IPostService postService, IUserService userService, ILogger<HomeBusinessManager> logger)
        {
            this.userService = userService;
            this.postService = postService;
            this.logger = logger;
        }

        public ActionResult<AuthorViewModel> GetAuthorViewModel(string authorId, string searchString, int? page)
        {
            if (authorId is null)
            {
                logger.LogError("HomeBusinessManager: GetAuthorViewModel BadRequestResult");
                return new BadRequestResult();
            }

            var user = userService.Get(authorId);

            if (user is null)
            {
                logger.LogError("HomeBusinessManager: GetAuthorViewModel NotFoundResult");
                return new NotFoundResult();
            }

            int size = 20;
            int number = page ?? 1;

            var posts = postService.GetPosts(searchString ?? string.Empty)
                .Where(post => post.Published && post.Creator == user);
            logger.LogInformation("HomeBusinessManager: GetAuthorViewModel OK");
            return new AuthorViewModel
            {
                Author = user,
                Posts = new StaticPagedList<Post>(posts.Skip((number - 1) * size).Take(size), number, size, posts.Count()),
                SearchString = searchString,
                PageNumber = number
            };
            
        }

        public ActionResult<CategoryViewModel> GetCategoryViewModel(int? categoryId, string searchString, int? page)
        {
            if (categoryId is null)
            {
                logger.LogError("HomeBusinessManager: GetCategoryViewModel BadRequestResult");
                return new BadRequestResult();
            }

            var category = postService.GetCategory(categoryId ?? 1);

            if (category is null)
            {
                logger.LogError("HomeBusinessManager: GetCategoryViewModel NotFoundResult");
                return new NotFoundResult();
            }

            int size = 20;
            int number = page ?? 1;

            var posts = postService.GetPosts(searchString ?? string.Empty)
                .Where(post => post.Published && post.Category == category);
            logger.LogInformation("HomeBusinessManager: GetCategoryViewModel OK");
            return new CategoryViewModel
            {
                Category = category,
                Posts = new StaticPagedList<Post>(posts.Skip((number - 1) * size).Take(size), number, size, posts.Count()),
                SearchString = searchString,
                PageNumber = number
            };
            
        }
    }
}
