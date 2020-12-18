using Microsoft.EntityFrameworkCore.Migrations;

namespace Blog111.Data.Migrations
{
    public partial class categoryview : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "category",
                table: "Posts",
                nullable: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "category",
                table: "Posts");
        }
    }
}
