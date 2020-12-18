using Blog111.Entities;
using Entities;
using PagedList.Core;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Blog111.Models.HomeViewModels
{
    public class AuthorViewModel
    {
        public User Author { get; set; }
        public IPagedList<Post> Posts {get; set;}
        public string SearchString { get; set; }
        public int PageNumber { get; set; }

    }
}
