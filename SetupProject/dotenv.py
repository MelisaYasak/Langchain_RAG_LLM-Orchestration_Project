from dotenv import load_dotenv, dotenv_values

#.env dosaysını arayıp içerisindeki değerlere erişebilmek için kullanılır.
load_dotenv()

print(dotenv_values(".env").get("LANGCHAIN_API_KEY"))