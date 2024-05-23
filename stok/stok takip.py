import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QListWidget, QListWidgetItem, QMessageBox

class Urun:
    def __init__(self, ad, stok_miktari):
        self.ad = ad
        self.stok_miktari = stok_miktari

    def urun_ekle(self, miktar):
        self.stok_miktari += miktar

    def siparis_olustur(self, miktar):
        if self.stok_miktari >= miktar:
            self.stok_miktari -= miktar
            return True
        else:
            return False

class Stok:
    def __init__(self):
        self.urunler = {}

    def urun_ekle(self, urun):
        self.urunler[urun.ad] = urun

    def stok_guncelle(self, ad, miktar):
        if ad in self.urunler:
            self.urunler[ad].urun_ekle(miktar)
            return True
        else:
            return False

    def stok_durumu_goruntule(self):
        stok_durumu = ""
        for ad, urun in self.urunler.items():
            stok_durumu += f"{ad}: {urun.stok_miktari}\n"
        return stok_durumu

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.stok = Stok()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Ürün Ekle
        layout_urun_ekle = QHBoxLayout()
        lbl_urun_ad = QLabel("Ürün Adı:")
        self.input_urun_ad = QLineEdit()
        layout_urun_ekle.addWidget(lbl_urun_ad)
        layout_urun_ekle.addWidget(self.input_urun_ad)

        lbl_stok_miktari = QLabel("Stok Miktarı:")
        self.input_stok_miktari = QLineEdit()
        layout_urun_ekle.addWidget(lbl_stok_miktari)
        layout_urun_ekle.addWidget(self.input_stok_miktari)

        btn_urun_ekle = QPushButton("Ürün Ekle")
        btn_urun_ekle.clicked.connect(self.urun_ekle)
        layout_urun_ekle.addWidget(btn_urun_ekle)
        layout.addLayout(layout_urun_ekle)

        # Sipariş Oluştur
        layout_siparis_olustur = QHBoxLayout()
        lbl_siparis_urun_ad = QLabel("Sipariş Verilen Ürün Adı:")
        self.input_siparis_urun_ad = QLineEdit()
        layout_siparis_olustur.addWidget(lbl_siparis_urun_ad)
        layout_siparis_olustur.addWidget(self.input_siparis_urun_ad)

        lbl_siparis_miktar = QLabel("Sipariş Miktarı:")
        self.input_siparis_miktar = QLineEdit()
        layout_siparis_olustur.addWidget(lbl_siparis_miktar)
        layout_siparis_olustur.addWidget(self.input_siparis_miktar)

        btn_siparis_olustur = QPushButton("Sipariş Oluştur")
        btn_siparis_olustur.clicked.connect(self.siparis_olustur)
        layout_siparis_olustur.addWidget(btn_siparis_olustur)
        layout.addLayout(layout_siparis_olustur)

        # Stok Durumunu Görüntüle
        self.text_stok_durumu = QTextEdit()
        layout.addWidget(self.text_stok_durumu)

        # Butonlar
        layout_butonlar = QHBoxLayout()
        btn_stok_durumu = QPushButton("Stok Durumunu Görüntüle")
        btn_stok_durumu.clicked.connect(self.stok_durumu_goruntule)
        layout_butonlar.addWidget(btn_stok_durumu)

        btn_cikis = QPushButton("Çıkış")
        btn_cikis.clicked.connect(self.close)
        layout_butonlar.addWidget(btn_cikis)
        layout.addLayout(layout_butonlar)

        self.setLayout(layout)

    def urun_ekle(self):
        ad = self.input_urun_ad.text()
        stok_miktari = int(self.input_stok_miktari.text())
        urun = Urun(ad, stok_miktari)
        self.stok.urun_ekle(urun)
        QMessageBox.information(self, "Bilgi", "Ürün başarıyla eklendi.")

    def siparis_olustur(self):
        ad = self.input_siparis_urun_ad.text()
        miktar = int(self.input_siparis_miktar.text())
        if self.stok.urunler.get(ad):
            if self.stok.urunler[ad].siparis_olustur(miktar):
                QMessageBox.information(self, "Bilgi", "Sipariş başarıyla oluşturuldu.")
                return
        QMessageBox.warning(self, "Uyarı", "Ürün stokta bulunmamaktadır veya sipariş miktarı stok miktarından fazladır.")

    def stok_durumu_goruntule(self):
        stok_durumu = self.stok.stok_durumu_goruntule()
        self.text_stok_durumu.setPlainText(stok_durumu)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Arayuz()
    window.setWindowTitle("Stok Yönetim Sistemi")
    window.show()
    sys.exit(app.exec_())

