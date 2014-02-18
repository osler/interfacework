ChatFrame_MessageEventHandler2 = ChatFrame_MessageEventHandler
function ChatFrame_MessageEventHandler(s,e,arg1,...)
	if arg1 ~= nil then
		if arg1 ~= "" then
			if string.find(arg1, "[ADDON]", 1, true) ~= nil then
				if (arg1 == "[ADDON] test") then
					PlaySound("igSpellBookOpen");
				end
			end
		end
	end
	ChatFrame_MessageEventHandler2(s,e,arg1,...)
end