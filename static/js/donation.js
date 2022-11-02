document.addEventListener("DOMContentLoaded", async () => {
    
    

    const alertBox = document.getElementById('alert-box')
    const form = document.getElementById('donation-form')

    const csrf = document.getElementsByName('csrfmiddlewaretoken')

    const nameDiv = document.getElementById("name-div")
    const emailDiv = document.getElementById("email-div")
    const phoneDiv = document.getElementById("phone-div") 

    const someoneCheckbox = document.getElementById('id_donate_for_someone')

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var buttonList = document.getElementsByName("amount-button")

    for (let i = 0; i < buttonList.length; i++) {
        buttonList[i].addEventListener('click', ()=>{
            console.log(buttonList[i].value)
            document.getElementById('id_amount').value = buttonList[i].value
        })
    }

    someoneCheckbox.addEventListener('change', ()=>{
        if(someoneCheckbox.checked) {
            nameDiv.classList.remove("hidden")
            nameDiv.classList.add("flex")

            emailDiv.classList.remove("hidden")
            emailDiv.classList.add("flex")
            
            phoneDiv.classList.remove("hidden")
            phoneDiv.classList.add("flex")
        }
        else {
            nameDiv.classList.add("hidden")
            nameDiv.classList.remove("flex")

            emailDiv.classList.add("hidden")
            emailDiv.classList.remove("flex")
            
            phoneDiv.classList.add("hidden")
            phoneDiv.classList.remove("flex") 

        }
    })


    const response = await fetch("/battuta/country")
    const countries = await response.json()

    console.log(countries)

    const countrySelect = document.getElementById("id_country")
    const regionSelect = document.getElementById("id_region")

    const showRegions = async ()=> {
        regionSelect.innerHTML =""
        const code = countrySelect.value
        const response = await fetch(`/battuta/${code}`)
        const regions = await response.json()

        console.log(regions)
        

        for(let i=0; i<regions.length; i++) {
            regionSelect.innerHTML += `
        <option value="${regions[i].region}">${regions[i].region}</option>
        `
        }
    }
    // for first time after document is loaded
    showRegions()
    countrySelect.addEventListener('change', showRegions)

    const closeAlertS = document.getElementById('close-success-alert')
    const closeAlertE = document.getElementById('close-error-alert')   
    
    closeAlertS.addEventListener('click', async (event)=>{
        $('#full-success-alert')
        .delay(100)
        .fadeOut()
    })
    closeAlertE.addEventListener('click', async (event)=>{
        $('#full-error-alert')
        .delay(100)
        .fadeOut()
    })

    const paymentForm = document.getElementById('id_payment')

    form.addEventListener('submit', async (event)=>{
        event.preventDefault()

        const formData = {
            amount: parseInt( document.getElementById("id_amount").value)/10000,
            region: document.getElementById("id_region").value,
            country: document.getElementById("id_country").value,
            hopes: document.getElementById("id_hopes").value,
            donate_for_someone: document.getElementById("id_donate_for_someone").checked,
            name: document.getElementById("id_name").value,
            phone: document.getElementById("id_phone").value,
            email: document.getElementById("id_email").value,
        };

        var formDataobj = new FormData()
        formDataobj.append('amount', formData['amount']) 
        formDataobj.append('region', formData['region']) 
        formDataobj.append('country', formData['country']) 
        formDataobj.append('hopes', formData['hopes']) 
        formDataobj.append('donate_for_someone', formData['donate_for_someone']) 
        formDataobj.append('name', formData['name']) 
        formDataobj.append('phone', formData['phone']) 
        formDataobj.append('email', formData['email']) 
        formDataobj.append('payment', paymentForm.files[0]) 

        console.log(formData)
        console.log(formDataobj)

        console.log(JSON.stringify(formData))
        console.log(JSON.stringify(formDataobj))

        const response = await fetch("/donation/submit/", {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie("csrftoken"),
            },
            body: formDataobj,
            
        })
        
        const message = await response.json()
        const alertMessage = message.message
        console.log(message)
        console.log(alertMessage)

        let $fullAlert = ""
        let $alertMessage = ""
        if (alertMessage === "Successfully submitted") {
            $alertMessage = $('success-alert-message')
            $fullAlert = $('#full-success-alert')
        }
        else {
            $alertMessage = $('error-alert-message')
            $fullAlert = $('#full-error-alert')
        }

        document.getElementById('success-alert-message').innerText = `You just donated ${formData['amount']} trees in ${formData['region']}.
        ${[message.coin]} coins have been added to your account`

        document.getElementById('error-alert-message').innerText = `Please check the fields and make sure you have filled everything required correctly`
        $('html, body').animate({ scrollTop: 0 }, 'fast');

        $fullAlert 
        .delay(100)
        .fadeIn()
        .delay(3000)
        .fadeOut()

        form.reset()
    })




    
})