using Blog111.Entities;
using Entities;
using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;

namespace Services.Interfaces
{
    public interface IPostService
    {
        Task<Post> Add(Post post);
        Task<Comment> Add(Comment comment);
        Comment GetComment(int commentID);
        IEnumerable<Post> GetPosts(User user);
        Post GetPost(int PostID);
        Task<Post> Update(Post post);
        Task<Category> AddCategory(Category category);
        Category GetCategory(int id);
        Category GetCategory(string title);
        IEnumerable<Post> GetPosts(string search);
        List<Category> GetCategories();
        
    }
}
