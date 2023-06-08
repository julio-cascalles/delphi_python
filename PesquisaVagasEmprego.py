import os
from delphifmx import *

class frmPesquisaVagasEmprego(Form):

    def __init__(self, owner):
        self.grp_linguagem = None
        self.lbl_backend = None
        self.cbx_backend = None
        self.lbl_frontend = None
        self.cbx_frontend = None
        self.grp_local = None
        self.chk_presencial = None
        self.chk_remoto = None
        self.chk_hibrido = None
        self.grp_data = None
        self.rad_qualquer = None
        self.rad_semana = None
        self.rad_mes = None
        self.rad_24horas = None
        self.pan_palavras = None
        self.lbl_palavras = None
        self.edt_palavras = None
        self.btn_limpar = None
        self.btn_Exibir = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "PesquisaVagasEmprego.pyfmx"))

    def limpa_filtros(self, Sender):
        self.cbx_backend.ItemIndex = -1
        self.cbx_frontend.ItemIndex = -1
        self.chk_presencial.IsChecked = False
        self.chk_remoto.IsChecked = False
        self.chk_hibrido.IsChecked = False
        self.rad_qualquer.IsChecked = False
        self.rad_mes.IsChecked = False
        self.rad_semana.IsChecked = False
        self.rad_24horas.IsChecked = False
        self.edt_palavras.Text = ''

def main():
    Application.Initialize()
    Application.Title = 'Pesquisa de vagas de emprego'
    Application.MainForm = frmPesquisaVagasEmprego(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()
