using Microsoft.EntityFrameworkCore.Migrations;

namespace Blog111.Data.Migrations
{
    public partial class categoryview2 : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "category",
                table: "Posts");

            migrationBuilder.AddColumn<string>(
                name: "category_string",
                table: "Posts",
                nullable: true);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "category_string",
                table: "Posts");

            migrationBuilder.AddColumn<string>(
                name: "category",
                table: "Posts",
                type: "nvarchar(max)",
                nullable: true);
        }
    }
}
