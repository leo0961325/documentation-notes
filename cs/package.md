# Net Core 套件管理

- 2019/01/31
- v2.2

```sh
### 安裝套件至 PROJ.csproj

$# dotnet add package Microsoft.EntityFrameworkCore.Sqlite     # SQLite
$# dotnet add package MySql.Data.EntityFrameworkCore           # MySQL
$# dotnet add package Microsoft.EntityFrameworkCore.Design     # (ASP.net Core 預設已安裝此套建)

# dotnet ef CLI(若為 ASP.NET Core, 此已自動包含在內)
$# dotnet add package Microsoft.EntityFrameworkCore.Design
    # <PackageReference Include="Microsoft.EntityFrameworkCore.Design" Version="2.2.1" />

# 
$# dotnet add package Microsoft.EntityFrameworkCore.Sqlite
    # <PackageReference Include="Microsoft.EntityFrameworkCore.Sqlite" Version="2.2.1" />

# 
$# dotnet add package Microsoft.VisualStudio.Web.CodeGeneration.Tools
    # <PackageReference Include="Microsoft.VisualStudio.Web.CodeGeneration.Tools" Version="2.0.4" />

# 
$# dotnet add package Microsoft.VisualStudio.Web.CodeGeneration.Design
    # <PackageReference Include="Microsoft.VisualStudio.Web.CodeGeneration.Design" Version="2.2.1" />

$# dotnet add package MySqlConnector
    # <PackageReference Include="MySqlConnector" Version="0.49.0" />
```





# DB

## Migrations

建立 Model 之後, 可使用 移轉(migrations) 來建立 Database

```sh
# 建立移轉結構(migrations/xxx)
dotnet ef migrations add InitialCreate

# 將新的移轉(migrations/xxx 套用至 DB)
dotnet ef database update

# undo migrations
dotnet ef migrations remove
```


## Implements

### SQLite 為例:

```cs
using (var db = new BloggingContext())
{
    db.Blogs.Add(new Blog { Url = "http://blogs.msdn.com/adonet" });
    var count = db.SaveChanges();
    Console.WriteLine("{0} records saved to database", count);

    Console.WriteLine();
    Console.WriteLine("All blogs in database:");
    foreach (var blog in db.Blogs)
    {
        Console.WriteLine(" - {0}", blog.Url);
    }
}
```

```cs
////// Startup.cs

// MySQL
services.AddDbContext<MovieContext>(options => 
  options.UseMySQL(Configuration.GetConnectionString("MovieContext")));

// SQL Server
optionsBuilder.UseSqlServer(
    "Server=(localdb)\mssqllocaldb;Database=MyDatabase;Trusted_Connection=True;");

protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    modelBuilder.Entity<Blog>()
        .ForSqlServerIsMemoryOptimized();
}
```