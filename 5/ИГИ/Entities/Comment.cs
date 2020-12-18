using Blog111.Entities;
using System;
using System.Collections.Generic;
using System.Text;

namespace Entities
{
    public class Comment
    {
        public int ID { get; set; }
        public Post Post { get; set; }
        public User Poster { get; set; }
        public string Content { get; set; }
        public Comment Parent { get; set; }
        public DateTime Create { get; set; }
        public virtual IEnumerable<Comment> Comments { get; set; }
    }
}
