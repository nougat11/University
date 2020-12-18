using Blog111.Entities;
using Entities;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Authorization.Infrastructure;
using Microsoft.AspNetCore.Identity;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Blog111.Authorization
{
    public class BlogAuthorizationHandler : AuthorizationHandler<OperationAuthorizationRequirement, Post>
    {
        private readonly UserManager<User> userManager;
        private readonly ILogger<BlogAuthorizationHandler> logger;
        public BlogAuthorizationHandler(UserManager<User> userManager, ILogger<BlogAuthorizationHandler> logger)
        {
            this.userManager = userManager;
            this.logger = logger;
        }
        protected override async Task HandleRequirementAsync(AuthorizationHandlerContext context, OperationAuthorizationRequirement requirement, Post resource)
        {
            var user = await userManager.GetUserAsync(context.User);
            if ((requirement.Name == Operations.Update.Name || requirement.Name == Operations.Delete.Name) && user == resource.Creator)
            {
                logger.LogInformation("Authorization Handler: Operation OK");
                context.Succeed(requirement);

            }
            if (requirement.Name == Operations.Read.Name && (!resource.Published) && user == resource.Creator)
            {
                logger.LogInformation("Authorization Handler: Operation OK");
                context.Succeed(requirement);
            }
           
        }
    }
}
