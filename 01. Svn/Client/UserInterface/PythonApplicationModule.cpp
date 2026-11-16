// void initapp() icinde:
// Ara:
	PyModule_AddIntConstant(poModule, "ENABLE_GROWTH_PET_RENEWAL", 0);

// Altina ekle:
#ifdef ENABLE_AUTO_CHAT
	PyModule_AddIntConstant(poModule, "ENABLE_AUTO_CHAT", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_AUTO_CHAT", 0);
#endif

