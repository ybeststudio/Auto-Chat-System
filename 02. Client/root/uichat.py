# ChatWindow.__init__ icinde ara:
		btnSendWhisper.Hide()
		self.btnSendWhisper = btnSendWhisper

# Altina ekle:
		if app.ENABLE_AUTO_CHAT:
			btnAutoChat = ui.Button()
			btnAutoChat.SetParent(self)
			btnAutoChat.SetUpVisual("d:/ymir work/ui/game/taskbar/auto_chat_norm.png")
			btnAutoChat.SetOverVisual("d:/ymir work/ui/game/taskbar/auto_chat_hover.png")
			btnAutoChat.SetDownVisual("d:/ymir work/ui/game/taskbar/auto_chat_select.png")
			btnAutoChat.SAFE_SetEvent(self.ToggleAutoChat)
			if app.ENABLE_EMOTICONS_SYSTEM:
				toolTipAutoChat = ui.Ballon()
				toolTipAutoChat.SetParent(self)
				toolTipAutoChat.SetPosition(0, -38)
				toolTipAutoChat.SetWindowHorizontalAlignCenter()
				toolTipAutoChat.Hide()
				toolTipAutoChat.SetText(localeInfo.AUTO_CHAT_TITLE)
				self.toolTipAutoChat = toolTipAutoChat
				btnAutoChat.SetToolTipWindow(self.toolTipAutoChat)
			else:
				btnAutoChat.SetToolTipText(localeInfo.AUTO_CHAT_TITLE)
			btnAutoChat.Hide()
			self.btnAutoChat = btnAutoChat


# ChatWindow.CloseChat icinde ara:
		self.btnChatLog.Hide()
		self.btnChatSizing.Hide()

# Altina ekle:
		if app.ENABLE_AUTO_CHAT and self.btnAutoChat:
			self.btnAutoChat.Hide()


# ChatWindow.OnUpdate icinde ara:
	def OnUpdate(self):

# Altina ekle:
		if app.ENABLE_AUTO_CHAT and self.interface and self.interface.wndAutoChat:
			self.interface.wndAutoChat.Tick()


# ChatWindow.__PlaceInputButtons icinde ara:
				self.btnEmoticonsOpen.SetPosition(self.GetWidth() - 100, 2 + lineHeight)
				self.btnEmoticonsClose.SetPosition(self.GetWidth() - 100, 2 + lineHeight)

# Altina ekle:
			if app.ENABLE_AUTO_CHAT and self.btnAutoChat:
				self.btnAutoChat.SetPosition(self.GetWidth() - 75, 2 + lineHeight)
				self.btnAutoChat.Show()


# ChatWindow icinde ara:
			(bx, by) = self.btnEmoticonsOpen.GetGlobalPosition()
			self.emojiPicker.Toggle(bx + self.btnEmoticonsOpen.GetWidth() - uiemojipicker.WIDTH, by - uiemojipicker.HEIGHT - 4)

# Altina ekle:
	if app.ENABLE_AUTO_CHAT:
		def ToggleAutoChat(self):
			if self.interface:
				self.interface.ToggleAutoChatWindow()

