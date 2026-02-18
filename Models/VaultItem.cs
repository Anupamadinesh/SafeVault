using System.ComponentModel.DataAnnotations;

namespace SafeVault.Models;

public class VaultItem
{
    public int Id { get; set; }

    [Required]
    [StringLength(200)]
    public string Secret { get; set; } = string.Empty;
}
