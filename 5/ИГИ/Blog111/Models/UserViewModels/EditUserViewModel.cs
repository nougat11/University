using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Blog111.Models.UserViewModels
{
    public class EditUserViewModel
    {
        public string id { get; set; }
        public string Email { get; set; }
        
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Header { get; set; }

        public string content { get; set; }
    }
}
