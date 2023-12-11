import os
from delphifmx import *

class frmPesquisaVagasEmprego(Form):

    def __init__(self, owner):
        self.LoadProps(
            os.path.join(os.path.dirname(os.path.abspath(
                __file__)), "PesquisaVagasEmprego.pyfmx"
            ))

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


if __name__ == '__main__':
    Application.Initialize()
    Application.Title = 'Pesquisa de vagas de emprego'
    Application.MainForm = frmPesquisaVagasEmprego(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()
