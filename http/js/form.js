$(function() {

    var execSuccess = function(execOutput) {
        $('#submitBtn').removeClass('loading').html('Save')
        $('#submitBtn').attr('disabled', false)
    }

    var populateForm = function() {
        var email = scraperwiki.sql("select value_blob from swvariables where name='recipient';", function(data, textStatus, jqXHR) {
            console.log("Success")
	    $('#email').val(data[0]['value_blob']);
        },
        function(jqXHR, textStatus, errorThrown) {
            console.log("Error! " + jqXHR + textStatus + errorThrown)   
        })
 
        var tableName = scraperwiki.sql("select value_blob from swvariables where name='tablename';", function(data, textStatus, jqXHR) {
            console.log("Success")
            $('#tablename').val(data[0]['value_blob'])
        },
        function(jqXHR, textStatus, errorThrown) {
            console.log("Error! " + jqXHR + textStatus + errorThrown)   
        })

        console.log(email.responseText)
        console.log(tableName)
    }
    
    $('#submitBtn').on('click', function() {
        $(this).attr('disabled', true)  // Disable further clicks.
        $(this).addClass('loading').html('Loading&hellip;')  // Spinny loader.
        var email = $('#email').val()
        var tableName = $('#tablename').val()
        var endpointUrl = scraperwiki.readSettings().source.url + '/sqlite?q=select count(*) from ' + tableName + ';'
        console.log(scraperwiki.shellEscape('/home/tool/http/update_json.py ' + email + ' ' + endpointUrl + ' '  + tableName))
        scraperwiki.exec('/home/tool/http/update_json.py ' + email + ' ' + scraperwiki.shellEscape(endpointUrl) + ' '  + tableName, execSuccess)
    })
  $(document).ready(function(){
    populateForm()
  })
})


