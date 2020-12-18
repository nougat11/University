using Blog111.Entities;
using System;
using System.Collections.Generic;
using System.Text;

namespace Entities
{
    public class Post
    {
        public virtual IEnumerable<Comment> Comments { get; set; }
        public int ID { get; set; }
        public User Creator { get; set; }
        public User Approver { get; set; }
        public Category Category { get; set; }
        public string Title { get; set; }
        public string Content { get; set; }
        public string category_string { get; set; }
        public DateTime Create { get; set; }
        public DateTime Update { get; set; }
        public bool Published { get; set; }
        public bool Approved { get; set; }
        
        
    }
}
