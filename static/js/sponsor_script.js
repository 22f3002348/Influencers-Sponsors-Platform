document.getElementById("New").addEventListener("click",function(){
    const newcampaign = document.getElementById("newcampaign");
    newcampaign.style.display = "block";
})

document.getElementById("Cancel").addEventListener("click",function(){
    const newcampaign = document.getElementById("newcampaign");
    newcampaign.style.display = "none";
}) 

document.getElementById("edit-profile").addEventListener("click",function(){
    const editp = document.getElementById("editprofile");
    editp.style.display = "block";
})

document.getElementById("cancelprofile").addEventListener("click",function(){
    const cancelp = document.getElementById("editprofile");
    cancelp.style.display = "none";
})

document.querySelectorAll(".edit-campaign").forEach(function(button) {
    button.addEventListener("click", function() {
        const editcampaign = button.closest(".showcampaigns");
        const editdetails = editcampaign.querySelector(".editexistingcampaigns");
        if (editdetails.style.display === "none" || editdetails.style.display === "") {
            editdetails.style.display = "block";
        }  
    });
});

document.querySelectorAll(".view-campaign").forEach(function(button) {
    button.addEventListener("click", function() {
        const campaign = button.closest(".showcampaigns");
        const campaigndetails = campaign.querySelector(".showexistingcampaigns");
        if (campaigndetails.style.display === "none" || campaigndetails.style.display === "") {
            campaigndetails.style.display = "block";
        }  
    });
});

document.querySelectorAll(".ad-request").forEach(function(button) {
    button.addEventListener("click", function() {
        const request = button.closest(".showexistingcampaigns");
        const requestdetails = request.querySelector(".Ad-Request");
        if (requestdetails.style.display === "none" || request.style.display === "") {
            requestdetails.style.display = "block";
        }  
    });
});

document.querySelectorAll(".edit-request").forEach(function(button) {
    button.addEventListener("click", function() {
        const editad = button.closest(".showrequests");
        const editaddetails = editad.querySelector(".Edit-Ad-Request");
        if (editaddetails.style.display === "none" || editaddetails.style.display === "") {
            editaddetails.style.display = "block";
        }  
    });
});

document.querySelectorAll('.cancel-edit').forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault(); 
        const canceledit = button.closest('.editexistingcampaigns'); 
        canceledit.style.display = 'none'; 
    });
});

document.querySelectorAll('.cancel-request').forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault(); 
        const cancelrequest = button.closest('.Ad-Request'); 
        cancelrequest.style.display = 'none'; 
    });
});

document.querySelectorAll('.close-campaign').forEach(function(button) {
    button.addEventListener("click", function() {
        const closecampaign = button.closest(".showcampaigns");
        const closecampaigndetails = closecampaign.querySelector(".showexistingcampaigns");
        closecampaigndetails.style.display ="none";
    });
});

document.querySelectorAll('.cancel-request-edit').forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault(); 
        const cancelrequestedit = button.closest('.Edit-Ad-Request'); 
        cancelrequestedit.style.display = 'none'; 
    });
});

document.querySelectorAll(".view-request").forEach(function(button) {
    button.addEventListener("click", function() {
        const receivedrequest = button.closest(".showreceivedrequests");
        const receivedrequestdetails = receivedrequest.querySelector(".showexistingreceivedrequests");
        if (receivedrequestdetails.style.display === "none" || receivedrequestdetails.style.display === "") {
            receivedrequestdetails.style.display = "block";
        }  
    });
});

document.querySelectorAll('.close-request').forEach(function(button) {
    button.addEventListener("click", function() {
        const closerequest = button.closest(".showreceivedrequests");
        const closerequestdetails = closerequest.querySelector(".showexistingreceivedrequests");
        closerequestdetails.style.display ="none";
    });
});

setTimeout(function() {
    var a = document.getElementById("alert");
    if (a) {
        a.style.display = 'none';
    }
}, 3000);