using System;
using System.Collections.Generic;
using System.Text;

namespace Entities
{
    public class Category
    {
        public int ID { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }
        public virtual IEnumerable<Post> Posts { get; set; }

    }
}
