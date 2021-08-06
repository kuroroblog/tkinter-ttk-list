import tkinter as tk
from tkinter import ttk

class Application(tk.Frame):
    # spinbox Widgetを取得する関数
    def getSpinbox(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、spinbox Widgetを作成する。
        # Spinboxについて : https://kuroro.blog/python/CQZWZZXhhyD3B1TWP3FN/
        spinbox = tk.Spinbox(frame)
        # frame Widget(Frame)を親要素として、spinbox Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        spinbox.pack(pady=10)

        # ttk.Spinbox()の外観を変更
        style = ttk.Style()
        # テーマ(名前)の指定を行う。
        # テーマ(名前)について : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/ ページの「テーマ(名前)を利用して、button Widgetの外観を変更」箇所を参照
        style.theme_use('classic')

        # frame Widget(Frame)を親要素として、spinbox Widgetを作成する。
        # Spinboxについて : https://kuroro.blog/python/CQZWZZXhhyD3B1TWP3FN/
        ttkSpinbox = ttk.Spinbox(frame)
        # frame Widget(Frame)を親要素として、spinbox Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        ttkSpinbox.pack()

    # scrollbar Widgetを取得する関数
    def getScrollBar(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack(pady=10)

        # frame Widget(Frame)を親要素として、text Widgetを作成する。
        # height : 高さを設定
        # width : 幅を設定
        # Textについて : https://kuroro.blog/python/bK6fWsP9LMqmER1CBz9E/
        text = tk.Text(frame, height=4, width=10)

        # frame Widget(Frame)を親要素として、scrollbar Widgetを作成する。
        # orient option : 垂直scrollbarを作成するため、tk.VERTICALを設定。水平scrollbarの場合は、tk.HORIZONTALを設定する。
        # command option : scrollbar Widgetを動かした場合に、連動して表示する内容を設定。今回は、text Widgetをy軸方向へ動かした内容を表示する。
        # Scrollbarについて : https://kuroro.blog/python/vgx53M7D1d6C0R8ejp0V/
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)

        # scrollbar Widgetをtext Widgetに反映する。
        # scrollbar Widgetの設定内容をtext Widgetと紐付ける。
        # yscrollcommand : text Widget内で上下移動した場合に、scrollbarが追従するように設定する。
        text["yscrollcommand"] = scrollbar.set

        # frame Widget(Frame)を親要素とした場合に、text Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        text.grid(row=0, column=0)
        # frame Widget(Frame)を親要素とした場合に、scrollbar Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # frame Widget(Frame)を親要素として、text Widgetを作成する。
        # height : 高さを設定
        # width : 幅を設定
        # Textについて : https://kuroro.blog/python/bK6fWsP9LMqmER1CBz9E/
        textForTtkScrollvar = tk.Text(frame, height=4, width=10)

        # ttk.Scrollbar()の外観を変更
        style = ttk.Style()
        # テーマ(名前)の指定を行う。
        # テーマ(名前)について : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/ ページの「テーマ(名前)を利用して、button Widgetの外観を変更」箇所を参照
        style.theme_use('classic')

        # frame Widget(Frame)を親要素として、scrollbar Widgetを作成する。
        # orient option : 垂直scrollbarを作成するため、tk.VERTICALを設定。水平scrollbarの場合は、tk.HORIZONTALを設定する。
        # command option : scrollbar Widgetを動かした場合に、連動して表示する内容を設定。今回は、text Widgetをy軸方向へ動かした内容を表示する。
        # Scrollbarについて : https://kuroro.blog/python/vgx53M7D1d6C0R8ejp0V/
        ttkScrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=textForTtkScrollvar.yview)

        # scrollbar Widgetをtext Widgetに反映する。
        # scrollbar Widgetの設定内容をtext Widgetと紐付ける。
        # yscrollcommand : text Widget内で上下移動した場合に、scrollbarが追従するように設定する。
        textForTtkScrollvar["yscrollcommand"] = ttkScrollbar.set

        # frame Widget(Frame)を親要素とした場合に、text Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        textForTtkScrollvar.grid(row=1, column=0)
        # frame Widget(Frame)を親要素とした場合に、scrollbar Widgetをどのように配置するのか?
        # gridについて : https://kuroro.blog/python/JoaowDiUdLAOj3cSBxiX/
        ttkScrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))

    # scale Widgetを取得する関数
    def getScale(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、scale Widgetを作成する。
        # Scaleについて : https://kuroro.blog/python/DUvG7YaE2i6jLwCxdPXJ/
        scale = tk.Scale(frame)
        # frame Widget(Frame)を親要素として、scale Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        scale.pack(pady=10)

        # ttk.Scale()の外観を変更
        style = ttk.Style()
        # テーマ(名前)の指定を行う。
        # テーマ(名前)について : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/ ページの「テーマ(名前)を利用して、button Widgetの外観を変更」箇所を参照
        style.theme_use('classic')

        # frame Widget(Frame)を親要素として、scale Widgetを作成する。
        # Scaleについて : https://kuroro.blog/python/DUvG7YaE2i6jLwCxdPXJ/
        ttkScale = ttk.Scale(frame)
        # frame Widget(Frame)を親要素として、scale Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        ttkScale.pack()

    # radiobutton Widgetを取得する関数
    def getRadiobutton(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、radiobutton Widgetを作成する。
        # text : テキスト情報
        # Radiobuttonについて : https://kuroro.blog/python/ztJbt5uabbTBMCGcljHc/
        radiobutton = tk.Radiobutton(frame, text="test")
        # frame Widget(Frame)を親要素として、radiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        radiobutton.pack(pady=10)

        # ttk.Radiobutton()の外観を変更
        style = ttk.Style()
        # テーマ(名前)の指定を行う。
        # テーマ(名前)について : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/ ページの「テーマ(名前)を利用して、button Widgetの外観を変更」箇所を参照
        style.theme_use('classic')

        # frame Widget(Frame)を親要素として、radiobutton Widgetを作成する。
        # text : テキスト情報
        # Radiobuttonについて : https://kuroro.blog/python/ztJbt5uabbTBMCGcljHc/
        ttkRadiobutton = ttk.Radiobutton(frame, text="test")
        # frame Widget(Frame)を親要素として、radiobutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        ttkRadiobutton.pack()

    # menubutton Widgetを取得する関数
    def getMenubutton(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、menubutton Widgetを作成する。
        # text : テキスト情報
        # Menubuttonについて : https://kuroro.blog/python/Dfq4VCJ7OiEfYJv6ySge/
        menubutton = tk.Menubutton(frame, text="test")
        # frame Widget(Frame)を親要素として、menubutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        menubutton.pack(pady=10)

        # ttk.Menubutton()の外観を変更
        style = ttk.Style()
        # テーマ(名前)の指定を行う。
        # テーマ(名前)について : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/ ページの「テーマ(名前)を利用して、button Widgetの外観を変更」箇所を参照
        style.theme_use('classic')

        # frame Widget(Frame)を親要素として、menubutton Widgetを作成する。
        # text : テキスト情報
        # Menubuttonについて : https://kuroro.blog/python/Dfq4VCJ7OiEfYJv6ySge/
        ttkMenubutton = ttk.Menubutton(frame, text="test")
        # frame Widget(Frame)を親要素として、menubutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        ttkMenubutton.pack()

    # label Widgetを取得する関数
    def getLabel(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(frame, text="test", width=10)
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label.pack(pady=10)

        # ttk.Label()の外観を変更
        style = ttk.Style()
        # テーマ(名前)の指定を行う。
        # テーマ(名前)について : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/ ページの「テーマ(名前)を利用して、button Widgetの外観を変更」箇所を参照
        style.theme_use('classic')

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        ttkLabel = ttk.Label(frame, text="test", width=10)
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        ttkLabel.pack()

    # entry Widgetを取得する関数
    def getEntry(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、entry Widgetを作成する。
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        entry = tk.Entry(frame)
        # frame Widget(Frame)を親要素として、entry Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        entry.pack(pady=10)

        # ttk.Entry()の外観を変更
        style = ttk.Style()
        # テーマ(名前)の指定を行う。
        # テーマ(名前)について : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/ ページの「テーマ(名前)を利用して、button Widgetの外観を変更」箇所を参照
        style.theme_use('classic')

        # frame Widget(Frame)を親要素として、entry Widgetを作成する。
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        ttkEntry = ttk.Entry(frame)
        # frame Widget(Frame)を親要素として、entry Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        ttkEntry.pack()

    # checkbutton Widgetを取得する関数
    def getCheckbutton(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、checkbutton Widgetを作成する。
        # text : テキスト情報
        # Checkbuttonについて : https://kuroro.blog/python/gspi4F2pMIkzHN7l0f1F/
        checkbutton = tk.Checkbutton(frame, text="tkinter checkbutton")
        # frame Widget(Frame)を親要素として、checkbutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        checkbutton.pack(pady=10)

        # ttk.Checkbutton()の外観を変更
        style = ttk.Style()
        # テーマ(名前)の指定を行う。
        # テーマ(名前)について : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/ ページの「テーマ(名前)を利用して、button Widgetの外観を変更」箇所を参照
        style.theme_use('classic')

        # frame Widget(Frame)を親要素として、checkbutton Widgetを作成する。
        # text : テキスト情報
        # Checkbuttonについて : https://kuroro.blog/python/gspi4F2pMIkzHN7l0f1F/
        ttkCheckbutton = ttk.Checkbutton(frame, text="test")
        # frame Widget(Frame)を親要素として、checkbutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        ttkCheckbutton.pack()

    # button Widgetを取得する関数
    def getButton(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        button = tk.Button(frame, text="tkinter button", width=10)
        # frame Widget(Frame)を親要素として、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        button.pack(pady=10)

        # ttk.Button()の外観を変更
        style = ttk.Style()
        # テーマ(名前)の指定を行う。
        # テーマ(名前)について : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/ ページの「テーマ(名前)を利用して、button Widgetの外観を変更」箇所を参照
        style.theme_use('classic')

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        ttkButton = ttk.Button(frame, text="ttk button", width=10)
        # frame Widget(Frame)を親要素として、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        ttkButton.pack()

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # self.getButton()
        # self.getCheckbutton()
        # self.getEntry()
        # self.getLabel()
        # self.getMenubutton()
        # self.getRadiobutton()
        # self.getScale()
        # self.getScrollBar()
        # self.getSpinbox()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
