using Blog111.Data;
using Blog111.Entities;
using Entities;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Services.Interfaces
{
    public class PostService : IPostService
    {
        private readonly ApplicationDbContext applicationDbContext;
        
        public PostService(ApplicationDbContext applicationDbContext)
        {
            this.applicationDbContext = applicationDbContext;
            
        }
        public async Task<Post> Add(Post post)
        {
            applicationDbContext.Add(post);
            await applicationDbContext.SaveChangesAsync();
            
            return post;
        }
        public async Task<Category> AddCategory(Category category)
        {
            applicationDbContext.Add(category);
            await applicationDbContext.SaveChangesAsync();
            return category;
        }

        public async Task<Comment> Add(Comment comment)
        {
            applicationDbContext.Add(comment);
            await applicationDbContext.SaveChangesAsync();
            return comment;
        }

        public async Task<Post> Update(Post post)
        {
            applicationDbContext.Update(post);
            await applicationDbContext.SaveChangesAsync();
            return post;
        }
        public IEnumerable<Post> GetPosts(User user)
        {
            return applicationDbContext.Posts
                .Include(blog => blog.Creator)
                .Include(blog => blog.Approver)
                .Include(blog => blog.Comments)
                .Where(blog => blog.Creator == user);
        }
        public List<Category> GetCategories()
        {

            var cat = applicationDbContext.Categories;
            List<Category> categories = cat.ToList();
            return categories;

        }

        public Category GetCategory(string title)
        {
            return applicationDbContext.Categories
                .FirstOrDefault(p => p.Title == title);

        }
        public Category GetCategory(int id)
        {
            return applicationDbContext.Categories
                .FirstOrDefault(p => p.ID == id);

        }
        public IEnumerable<Post> GetPosts(string search)
        {
            return applicationDbContext.Posts
                .OrderByDescending(Blog => Blog.Update)
                .Include(blog => blog.Creator)
                .Include(blog => blog.Comments)
                .Where(blog => blog.Title.Contains(search) || blog.Content.Contains(search));
        }

        public Post GetPost(int PostID)
        {
            return applicationDbContext.Posts
                .Include(post => post.Creator)
                .Include(post => post.Comments)
                    .ThenInclude(comment => comment.Poster)
                .Include(post => post.Comments)
                    .ThenInclude(comment=>comment.Comments)
                        .ThenInclude(reply => reply.Parent)
                .FirstOrDefault(post => post.ID == PostID);
        }

        public Comment GetComment(int commentID)
        {
            return applicationDbContext.Comments
                .Include(comment => comment.Poster)
                .Include(comment => comment.Content)
                //.Include(comment => comment.Parent)
                .FirstOrDefault(comment => comment.ID == commentID);
        }
    }
}
