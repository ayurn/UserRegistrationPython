class EmailTest:
    validMailIds = ["abc@yahoo.com", "abc-100@yahoo.com",
                    "abc.100@yahoo.com", "abc111@abc.com", "abc-100@abc.net", "abc.100@abc.com.au", "abc@1.com",
                    "abc@gmail.com.com", "abc+100@gmail.com"]

    invalidMmailIds = ["abc@.com.my", "abc123@gmail.a", "abc123@.com",
                       "abc123@.com.com", ".abc@abc.com", "abc()*@gmail.com", "abc..2002@gmail.com", "abc.@gmail.com",
                       "abc@abc@gmail.com", "abc@gmail.com.1a", "abc@gmail.com.aa.au"]
