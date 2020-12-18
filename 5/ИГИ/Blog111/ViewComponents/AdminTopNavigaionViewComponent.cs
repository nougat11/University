﻿using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Blog111.ViewComponents
{
    [ViewComponent(Name = "AdminTopNavigation")]
    public class AdminTopNavigationViewComponent : ViewComponent
    {
        public async Task<IViewComponentResult> InvokeAsync()
        {
            return await Task.Factory.StartNew(() => { return View(); });
        }
    }
}
