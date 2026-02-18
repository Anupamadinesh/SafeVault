using System.ComponentModel.DataAnnotations;

namespace SafeVault.Models;

public class LoginRequest
{
    [Required, StringLength(50)]
    public string Username { get; set; }

    [Required, StringLength(100)]
    public string Password { get; set; }
}
