<script lang='ts'>
  export let sport: string = ''

  type dialog =  {
    question: string,
    answer: string
  }

  let dialogs: dialog[] = []


  const loadAnswer = async (e: any) => {
    try {
      let question;
      const formData = new FormData(e.target)
		  for (let field of formData) {
			  const [key, value] = field
        if (key === 'question')
          question = value.toString()
		  }
      if (!question)
        return
      const res = await fetch('http://127.0.0.1:8000/openai_service/' + sport, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify({question: question})
      })
      if (!res.ok) {
        throw new Error("Network response was not ok");
      }
    

      const reader = res.body!.getReader();

      while (true) {
        const {done, value} = await reader.read();
        if (!done) {
          const answer = new TextDecoder().decode(value);
          dialogs = [{question: question, answer: answer}, ...dialogs]
        }
        if (done) {
          break;
        }
        
      }
    } catch (error) {
      console.error("Error:", error);
    }
    document.getElementById("question").reset();
  }


</script>

<div>
<form id="question" on:submit|preventDefault={loadAnswer}>
  <input class="input_field" name="question" type="text" placeholder="ask question about {sport}"/>
</form>
  {#each dialogs as dialog}
    <p class="question">Q: {dialog.question}</p>
    <p class="answer">R: {dialog.answer}</p>
  {/each}
</div>

<style>

  .input_field {
    font-size:1.2em;
  }
  .answer {
    font-size:1.25em;
  }

  .question {
    font-size:1.25em;
  }


</style>
