# 流程圖

- [Markdown Mermaid for VSCode](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)

帥!

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

- [Draw Diagrams With Markdown](https://support.typora.io/Draw-Diagrams-With-Markdown/)
```mermaid
%% Example of sequence diagram
  sequenceDiagram
    Alice->>Bob: Hello Bob, how are you?
    alt is sick
    Bob->>Alice: Not so good :(
    else is well
    Bob->>Alice: Feeling fresh like a daisy
    end
    opt Extra response
    Bob->>Alice: Thanks for asking
    end
```