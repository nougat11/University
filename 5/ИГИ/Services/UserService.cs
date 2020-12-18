using Blog111.Data;
using Blog111.Entities;
using Services.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Services
{
    public class UserService: IUserService
    {
        private readonly ApplicationDbContext applicationDbContext;

        public UserService(ApplicationDbContext applicationDbContext)
        {
            this.applicationDbContext = applicationDbContext;
        }

        public User Get(string id)
        {
            return applicationDbContext.Users.FirstOrDefault(user => user.Id == id);
        }

        public async Task<User> Update(User user)
        {
            applicationDbContext.Update(user);
            await applicationDbContext.SaveChangesAsync();
            return user;
        }
    }
}
