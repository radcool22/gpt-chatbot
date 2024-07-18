from openai import OpenAI
client = OpenAI(api_key="")

file = client.files.create(
    file=open("Semester_2_Final_Report_Grade_9_Gupta_Kabir_2024-05-28.pdf", "rb"),
    purpose = "assistants"
)
print(file)

assistant = client.beta.assistants.create(
    name = "Report Reader",
    instructions = "Act like an International Baccalaureate school teacher. Your role is to assess a student's performance based on a report card and give them advice on their performance and provide strengths and weaknesses and grade their assessment and provide their summary in a readable manner. You should be able to help the student to understand and improve based on the report uploaded.",
    tools = [{"type": "code_interpreter"}],
    model = "gpt-4o",
    file_ids = "file-SjOoIXRaIwC1d3pQzRvqj64j"
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
        thread_id = thread.id,
        role = "user",
        content = "What is the name of the student?"
    )

run = client.beta.threads.runs.create(
        thread_id = thread.id,
        assistant_id = assistant.id,
    )

run = client.beta.threads.runs.retrieve(
        thread_id = thread.id,
        run_id = run.id,
    )

messages = client.beta.threads.messages.list(
        thread_id = thread.id
    )

for message in messages.data:
    print(message.role + ": " + message.content[0].text.value)
