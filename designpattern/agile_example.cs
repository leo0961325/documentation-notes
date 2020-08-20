// 第一版本需求: 印表機要能印出鍵盤輸入的東西
// 第二版本需求: 磁帶機要能印出鍵盤輸入的東西
//      為了敏捷開發, 不對將來做預測, 所以不去預想將來可能輸出也要有變化
//      基於敏捷精神, 要去分析元件之間的 設計原則, 並用 設計原則 來分析問題

interface Reader
{
    int Read();
}

class KeyboardReader : Reader
{
    int Read()
        return Keyboard.Read();
}

class Copier 
{
    public static Reader reader = new KeyboardReader();
    public static void Copy()
    {
        int c;
        while ((c = reader.Read()) != -1)
        {
            punchFlag ? PaperTage.Write(c) : Printer.Write(c);
        }
    }
}