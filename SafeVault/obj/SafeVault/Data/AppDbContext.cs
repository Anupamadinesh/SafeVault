using Microsoft.EntityFrameworkCore;
using SafeVault.Models;
using System.Security.Cryptography;
using System.Text;

namespace SafeVault.Data;

public class AppDbContext : DbContext
{
    public DbSet<User> Users { get; set; }
    public DbSet<VaultItem> VaultItems { get; set; }

    public AppDbContext(DbContextOptions<AppDbContext> options)
        : base(options)
    {
        Database.EnsureCreated();

        if (!Users.Any())
        {
            Users.Add(new User
            {
                Username = "admin",
                PasswordHash = HashPassword("admin123"),
                Role = "Admin"
            });

            SaveChanges();
        }
    }

    private static string HashPassword(string password)
    {
        using var sha = SHA256.Create();
        var bytes = sha.ComputeHash(Encoding.UTF8.GetBytes(password));
        return Convert.ToBase64String(bytes);
    }
}
