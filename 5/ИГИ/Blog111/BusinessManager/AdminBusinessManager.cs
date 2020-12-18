using Blog111.Entities;
using Blog111.Models.AdminViewModels;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Identity;
using Microsoft.Extensions.Logging;
using Services.Interfaces;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Claims;
using System.Threading.Tasks;

namespace Blog111.BusinessManager.Interfaces
{
    public class AdminBusinessManager:IAdminBusinessManager
    {
        private UserManager<User> userManager;
        private IPostService postServise;
        private IUserService userService;
        private IWebHostEnvironment webHostEnvironment;
        private ILogger<AdminBusinessManager> logger;

        public AdminBusinessManager(UserManager<User> userManager, IPostService postService, IUserService userService, IWebHostEnvironment webHostEnvironment, ILogger<AdminBusinessManager> logger)
        {
            this.userManager = userManager;
            this.postServise = postService;
            this.userService = userService;
            this.webHostEnvironment = webHostEnvironment;
            this.logger = logger;
        }

        public async Task<IndexViewModel> GetAdminDashboard(ClaimsPrincipal claimsPrincipal)
        {
            var user = await userManager.GetUserAsync(claimsPrincipal);
            logger.LogInformation("AdminBusinessManager: GetAdminDashboard OK");
            return new IndexViewModel
            {
                Posts = postServise.GetPosts(user)
            };
        }

        public async Task<AboutViewModel> GetAboutViewModel(ClaimsPrincipal claimsPrincipal)
        {
            var user = await userManager.GetUserAsync(claimsPrincipal);
            logger.LogInformation("AdminBusinessManager: GetAboutViewModel OK");
            return new AboutViewModel
            {
                user = user,
                Header = user.Header,
                Content = user.content
            };
        }

        public async Task UpdateAbout(AboutViewModel aboutViewModel, ClaimsPrincipal claimsPrincipal)
        {
            var user = await userManager.GetUserAsync(claimsPrincipal);
            user.Header = aboutViewModel.Header;
            user.content = aboutViewModel.Content;

            if (aboutViewModel.HeaderImage != null)
            {
                string path = webHostEnvironment.WebRootPath;
                string pathImage = $@"{path}\UserFiles\Users\{user.Id}\HeaderImage.jpg";
                EnsureFolder(pathImage);
                using (var fileStream = new FileStream(pathImage, FileMode.Create))
                {
                    await aboutViewModel.HeaderImage.CopyToAsync(fileStream);
                }
                logger.LogInformation("AdminBusinessManager: UpdateAbout Photo OK");
            }
            logger.LogInformation("AdminBusinessManager: UpdateAbout OK");
            await userService.Update(user);  
        }

        private void EnsureFolder(string path)
        {
            string directoryName = Path.GetDirectoryName(path);
            if (directoryName.Length > 0)
            {
                Directory.CreateDirectory(Path.GetDirectoryName(path));
            }
            logger.LogInformation("AdminBusinessManager: EnsureFolder Photo OK");
        }
    }
}
