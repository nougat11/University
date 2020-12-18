using Blog111.Data;
using Blog111.Entities;
using Entities;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.SignalR;
using Services.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Blog111.Hubs
{
    [Authorize]
    public class CommentsHub : Hub
    {
        private readonly IPostService postService;
        private readonly UserManager<User> userManager;
        ApplicationDbContext db;

        public CommentsHub(IPostService postService, UserManager<User> userManager, ApplicationDbContext db)
        {
            this.postService = postService;
            this.userManager = userManager;
            this.db = db;
        }
        public async Task AddToGroup(string groupName)
        {
            await Groups.AddToGroupAsync(Context.ConnectionId, groupName);
        }

        public async Task addComment(string postId, string message)
        {
            var user = await userManager.GetUserAsync(Context.User);
            if (userManager.FindByIdAsync(user.Id) != null)
            {
                //string first = user.Split(' ')[0];
                //string second = user.Split(' ')[1];
                int POSTID = Convert.ToInt32(postId);
                Comment comment = new Comment
                {
                    Post = db.Posts.FirstOrDefault(post => post.ID == POSTID),
                    Poster = user,
                    Create = DateTime.UtcNow,
                    Content = message
                };
                await Clients.Group(postId).SendAsync("addComment", postId, user.FirstName + " " + user.LastName, message);
                db.Comments.Add(comment);
                await db.SaveChangesAsync();
            }
        }
    }
}
