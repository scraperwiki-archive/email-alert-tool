$(function() {

    var execSuccess = function(execOutput) {
        var datasetUrl = '/dataset/' + scraperwiki.box
        scraperwiki.tool.redirect(datasetUrl)
    }

    var populateForm = function() {
        var email = scraperwiki.sql("select value_blob from swvariables where name='recipient';", function(data, textStatus, jqXHR) {
            console.log("Success")
        },
        function(jqXHR, textStatus, errorThrown) {
            console.log("Error! " + jqXHR + textStatus + errorThrown)   
        })
 
        var tableName = scraperwiki.sql("select value_blob from swvariables where name='tablename';", function(data, textStatus, jqXHR) {
            console.log("Success")
        },
        function(jqXHR, textStatus, errorThrown) {
            console.log("Error! " + jqXHR + textStatus + errorThrown)   
        })

        $('#email').val(email);
        $('#tablename').val(tableName);
        console.log(email)
        console.log(tableName)
    }
    
    $('#submit').on('click', function() {
        var email = $('#email').val()
        var tableName = $('#tablename').val()
        var endpointUrl = scraperwiki.readSettings().target.url + '/sqlite?q=select count(*) from ' + tableName + ';'

        scraperwiki.exec('../update_json.py ' + email + ' ' + endpointUrl + ' '  + tableName, execSuccess)
    })
  $(document).ready(function(){
    populateForm()
  })
})


