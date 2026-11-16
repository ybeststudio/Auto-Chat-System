# Interface.__init__ icinde ara:
		self.wndBraveCape = None
		self.wndChat = None

# Altina ekle:
		self.wndAutoChat = None


# Interface.MakeInterface icinde ara:
		self.__MakeGuildWindow()
		self.__MakeChatWindow()

# Altina ekle:
		if app.ENABLE_AUTO_CHAT:
			import uiautochat
			self.wndAutoChat = uiautochat.AutoChatWindow()
			self.wndAutoChat.BindInterface(self)


# Interface.MakeHyperlinkTooltip icinde, ilgili if blogunun sonuna ekle:
			elif "shop" == type and app.ENABLE_AUTO_CHAT:
				if len(tokens) > 1 and str(tokens[1]) != player.GetMainCharacterName():
					self.OpenWhisperDialog(str(tokens[1]))


# Interface.Close icinde ara:
		if self.wndChat:
			self.wndChat.Destroy()

# Altina ekle:
		if self.wndAutoChat:
			self.wndAutoChat.Destroy()
			self.wndAutoChat = None


# Interface icinde ara:
				self.wndInventory.Close()
				self.wndExpandedMoney.Hide()

# Altina ekle:
	if app.ENABLE_AUTO_CHAT:
		def ToggleAutoChatWindow(self):
			if self.wndAutoChat:
				self.wndAutoChat.Toggle()

