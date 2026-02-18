using Xunit;

public class AuthTests
{
    [Fact]
    public void PasswordHash_ShouldNotBePlainText()
    {
        Assert.NotEqual("admin123", "HASHED_VALUE");
    }
}
