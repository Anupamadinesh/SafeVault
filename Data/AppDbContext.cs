using Microsoft.EntityFrameworkCore;
using SafeVault.Models;
using System.Security.Cryptography;
using System.Text;

namespace SafeVault.Data;

public class AppDbContext : DbContext
{
    public DbSet<User> Users => Set<User>();
    public DbSet<VaultItem> VaultItems => Set<VaultItem>();

    public AppDbContext(DbContextOptions<AppDbContext> options)
        : base(options)
    {
        Database.EnsureCreated();

        // Seed default admin user if database is empty
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

    // Secure SHA256 hashing
    private static string HashPassword(string password)
    {
        using var sha = SHA256.Create();
        var bytes = sha.ComputeHash(Encoding.UTF8.GetBytes(password));
        return Convert.ToBase64String(bytes);
    }
}
