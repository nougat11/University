using Blog111.Entities;
using Entities;
using Microsoft.AspNetCore.Identity.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore;

namespace Blog111.Data
{
    public class ApplicationDbContext : IdentityDbContext<User>
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }
        public DbSet<Post> Posts { get; set; }
        public DbSet<Comment> Comments { get; set; }
        public DbSet<Category> Categories { get; set; }
        /*protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            string connection = "Data Source=tcp:blog111dbserver.database.windows.net,1433;Initial Catalog=Blog111_db;User Id=vladik@blog111dbserver;Password=Vveliki_228";
            optionsBuilder.UseSqlServer(connection, (b => b.MigrationsAssembly("Data")));
        }*/
    }
}
