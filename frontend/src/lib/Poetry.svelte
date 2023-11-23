<script lang='ts'>
  import axios from "axios";
  import '../interceptor.ts'
  export let poetry: string = ''

  let lastAnswer = ''
  let lastQuestion = ''
  let waiting = false
  
  let dialogs: {
    poetry: string;
    answer: string;
    question: string;
  }[] = []

  const loadAnswer = async (e: any) => {
    try {
      const refreshToken = await axios.get('http://localhost:8000/')
    } catch (e) {
      console.log('token refresh')
    }
    try {
      const formData = new FormData(e.target)
		  for (let field of formData) {
			  const [key, value] = field
        if (key === 'question')
          lastQuestion = value.toString()
		  }
      document.querySelector('.input_field').value = '';
      waiting = true
      if (!lastQuestion)
        return
      const res = await fetch('http://127.0.0.1:8000/openai_service/' + poetry, {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
          "Authorization": 'Bearer ' + localStorage.getItem('access_token')
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify({question: lastQuestion})
      })
      if (!res.ok) {
        throw new Error("Network response was not ok");
      }
    

      const reader = res.body!.getReader();


      lastAnswer = ''
      while (true) {
        const {done, value} = await reader.read();
        if (!done) {
          let ans = new TextDecoder().decode(value);
          const splitted = ans.split('\n')
          ans = splitted.join('<br>')
          lastAnswer += ans
        }
        if (done) {
          break;
        }
        
      }
    } catch (error) {
      console.error("Error:", error);
    }
    dialogs = [{poetry: poetry, question: lastQuestion, answer: lastAnswer}, ...dialogs]
    waiting = false
    lastQuestion = ''
    lastAnswer = ''
  }


</script>

<div>
<form id="question" on:submit|preventDefault={loadAnswer}>
  <input class="input_field" name="question" type="text" placeholder=""/>
</form>
{#if waiting}
  <p class='waiting_string'>Waiting for openai ...</p>
{/if}
    {#if lastQuestion !== ''}
    <p class="question">Q: {lastQuestion}</p>
    {/if}
    {#if lastAnswer !== ''}
    <p class="answer">{@html lastAnswer}</p>
    {/if}
    {#each dialogs as dialog}
    {#if poetry === dialog.poetry}
    <p class="question">Q: {dialog.question}</p>
    {#if dialog.answer}
    <p class="answer">{@html dialog.answer}</p>
    {/if}
    {/if}
    {/each}
</div>

<style>
  .input_field {
    font-size: 1.2em;
  }
  .answer {
    font-size: 1.25em;
  }

  .question {
    font-size: 1.25em;
  }

  .waiting_string {
    font-size: 1.5em;
    color: grey
  }

</style>
