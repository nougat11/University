using Blog111.Authorization;
using Blog111.BusinessManager.Interfaces;
using Blog111.Entities;
using Blog111.Models.BlogViewModels;
using Blog111.Models.HomeViewModels;
using Entities;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using PagedList.Core;
using Services.Interfaces;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Claims;
using System.Threading.Tasks;

namespace Blog111.BusinessManager
{
    public class PostBusinessManager : IPostBusinessManager
    {
        private readonly UserManager<User> userManager;
        private readonly IPostService postService;
        private readonly IWebHostEnvironment webHostEnvironment;
        private readonly IAuthorizationService authorizationService;
        private ILogger<PostBusinessManager> logger;
        public PostBusinessManager(UserManager<User> userManager, IPostService postService, IWebHostEnvironment webHostEnvironment, IAuthorizationService authorizationService, ILogger<PostBusinessManager> logger)
        {
           
            this.userManager = userManager;
            this.postService = postService;
            this.webHostEnvironment = webHostEnvironment;
            this.authorizationService = authorizationService;
            this.logger = logger;
        }
        public IndexViewModel GetIndexViewModel(string searchString, int? page)
        {
            int size = 5;
            int number = page ?? 1;
            var posts = postService.GetPosts(searchString ?? string.Empty);
            logger.LogInformation("PostBusinessManager: GetIndexViewModel model OK.");
            return new IndexViewModel
            {
                Posts = new StaticPagedList<Post>(posts.Skip((number - 1) * size), number, size, posts.Count()),
                SearchString = searchString,
                PageNumber = number
            };
        }

        public async Task<ActionResult<PostViewModel>> GetPostViewModel(int? id, ClaimsPrincipal claimsPrincipal)
        {
            if (id is null)
            {
                logger.LogError("PostBusinessManager: GetPostViewModel BadRequestResult");
                return new BadRequestResult();
            }

            var postID = id.Value;

            var post = postService.GetPost(postID);

            if(post is null)
            {
                logger.LogError("PostBusinessManager: GetPostViewModel NotFoundResult");
                return new NotFoundResult();
            }

            if (!post.Published)
            {
                var authorizationResult = await authorizationService.AuthorizeAsync(claimsPrincipal, post, Operations.Read);

                if (!authorizationResult.Succeeded) return DeterminateActionResult(claimsPrincipal);
            }
            logger.LogInformation("PostBusinessManager: GetPostViewModel  OK.");
            return new PostViewModel
            {
                Post = post,
                User = await userManager.GetUserAsync(claimsPrincipal)
            };
        }
        
        public async Task <Post> CreatePost(CreateViewModel createViewModel, ClaimsPrincipal claimsPrincipal)
        {
            Post post = createViewModel.Post;
            post.Creator = await userManager.GetUserAsync(claimsPrincipal);
            post.Create = DateTime.UtcNow;
            post.Update = DateTime.UtcNow;
            post.Category = postService.GetCategory(post.category_string);
            post = await postService.Add(post);
            string webRootPath = webHostEnvironment.WebRootPath;
            string pathToImage = $@"{webRootPath}\UserFiles\Blogs\{post.ID}\HeaderImage.jpg";
            EnsureFolder(pathToImage);
            using (var fileStream = new FileStream(pathToImage, FileMode.Create))
            {
                await createViewModel.BlogHeaderImage.CopyToAsync(fileStream);
            }
            logger.LogInformation("PostBusinessManager: CreatePost  OK.");
            return post;

        }
        public async Task<Category> CreateCategory(CreateCategoryViewModel createcategoryViewModel, ClaimsPrincipal claimsPrincipal)
        {
            Category category = createcategoryViewModel.Category;
            category = await postService.AddCategory(category);
            string webRootPath = webHostEnvironment.WebRootPath;
            string pathToImage = $@"{webRootPath}\UserFiles\Categories\{category.ID}\HeaderImage.jpg";
            EnsureFolder(pathToImage);
            using (var fileStream = new FileStream(pathToImage, FileMode.Create))
            {
                await createcategoryViewModel.BlogHeaderImage.CopyToAsync(fileStream);
            }
            logger.LogInformation("PostBusinessManager: CreateCategory  OK.");
            return category;

        }
        public async Task<ActionResult<Comment>> CreateComment(PostViewModel postViewModel, ClaimsPrincipal claimsPrincipal)
        {
            if (postViewModel.Post is null || postViewModel.Post.ID == 0)
            {
                logger.LogError("PostBusinessManager: CreateComment BadRequestResult");
                return new BadRequestResult();
            }

            var post = postService.GetPost(postViewModel.Post.ID);

            if (post is null)
            {
                logger.LogError("PostBusinessManager: CreateComment NotFoundResult");
                return new NotFoundResult();
            }
            var comment = postViewModel.Comment;
            comment.Poster = await userManager.GetUserAsync(claimsPrincipal);
            comment.Post = post;
            comment.Create = DateTime.UtcNow;

            if (comment.Parent != null)
            {
                comment.Parent = postService.GetComment(comment.Parent.ID);

            }
            logger.LogInformation("PostBusinessManager: CreateComment  OK.");
            return await postService.Add(comment);
        }
        public async Task<ActionResult<EditViewModel>> UpdatePost(EditViewModel editViewModel, ClaimsPrincipal claimsPrincipal)
        {
            var post = postService.GetPost(editViewModel.Post.ID);

            if (post is null)
            {
                logger.LogError("PostBusinessManager: UpdatePost NotFoundResult");
                return new NotFoundResult();
            }

            var authorizationResult = await authorizationService.AuthorizeAsync(claimsPrincipal, post, Operations.Update);

            if (!authorizationResult.Succeeded)
            {
                return DeterminateActionResult(claimsPrincipal);
            }
            post.Published = editViewModel.Post.Published;
            post.Title = editViewModel.Post.Title;
            post.Content = editViewModel.Post.Content;
            post.Update = DateTime.UtcNow;
            if (editViewModel.BlogHeaderImage != null)
            {
                string webRootPath = webHostEnvironment.WebRootPath;
                string pathToImage = $@"{webRootPath}\UserFiles\Blogs\{post.ID}\HeaderImage.jpg";
                EnsureFolder(pathToImage);
                using (var fileStream = new FileStream(pathToImage, FileMode.Create))
                {
                    await editViewModel.BlogHeaderImage.CopyToAsync(fileStream);
                }
            }
            logger.LogInformation("PostBusinessManager: UpdatePost  OK.");
            return new EditViewModel
            {
                Post = await postService.Update(post)
            };
        }

        public async Task<ActionResult<EditViewModel>> GetEditViewModel(int? id, ClaimsPrincipal claimsPrincipal)
        {
            if (id is null)
            {
                logger.LogError("PostBusinessManager: GetEditViewModel BadRequestResult");
                return new BadRequestResult();
            }
            var postId = id.Value;
            var blog = postService.GetPost(postId);
            if (blog is null)
            {
                logger.LogError("PostBusinessManager: GetEditViewModel NotFoundResult");
                return new NotFoundResult();
            }

            var authorizationResult = await authorizationService.AuthorizeAsync(claimsPrincipal, blog, Operations.Update);
            if (!authorizationResult.Succeeded)
            {
                return DeterminateActionResult(claimsPrincipal);
            }
            logger.LogInformation("PostBusinessManager: GetEditViewModel  OK.");
            return new EditViewModel
            {
                Post = blog
            };
        }

        private ActionResult DeterminateActionResult(ClaimsPrincipal claimsPrincipal)
        {
            if (claimsPrincipal.Identity.IsAuthenticated)
            {
                return new ForbidResult();
            }
            else
            {
                return new ChallengeResult();
            }
        }

        private void EnsureFolder(string path)
        {
            string directoryName = Path.GetDirectoryName(path);
            if (directoryName.Length > 0)
            {
                Directory.CreateDirectory(Path.GetDirectoryName(path));
            }
            logger.LogInformation("PostBusinessManager: EnsureFolder  OK.");
        }
        
    }
}
