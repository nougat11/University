using Entities;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc.Rendering;
using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Threading.Tasks;

namespace Blog111.Models.BlogViewModels
{
    public class CreateViewModel
    {
        [Required, Display(Name="Header Image")]
        public IFormFile BlogHeaderImage { get; set; }
        public Post Post { get; set; }
        public List<SelectListItem> Categories { get; set; }
    }
}
