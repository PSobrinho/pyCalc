'''
#############################################################
##Projeto experimental de uma calculadora utilizando 'kivy'##
#############################################################
'''

from kivy.app import App
from kivy.lang import Builder

# Configura o tamanho da tela
from kivy.core.window import Window
Window.size = (250, 525)

GUI = Builder.load_file("screen.kv") # Instancia a interface a partir do arquivo .kv

class pyCalc(App): # Cria a aplicação através da classe
	def build(self):
		return GUI # Carrega a interface

	def clear(self):
		self.root.ids['numberA'].text = '0'
		self.root.ids['numberB'].text = '0'

	def getNumberA(self):
		# Recupera o dado de entrada no campo 'numberA'
		a = float(self.root.ids['numberA'].text)
		return a

	def getNumberB(self):
		# Recupera o dado de entrada no campo 'numberB'
		b = float(self.root.ids['numberB'].text)
		return b

	def sum(self, a, b):
		# Função de soma
		c = a + b
		self.root.ids['result'].text = str(c)

	def sub(self, a, b):
		# Função de subtração
		c = a - b
		self.root.ids['result'].text = str(c)

	def mult(self, a, b):
		# Função de multiplicação
		c = a * b
		self.root.ids['result'].text = str(c)

	def div(self, a, b):
		# Função de divisão
		if not b == 0:
			c = a / b
			self.root.ids['result'].text = str(c)
		else:
			self.root.ids['result'].text = 'Invalid Operation'


pyCalc().run()