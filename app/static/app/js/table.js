$(document).ready(function() {


    var selected = [];
    var dt_table = $('.datatable').dataTable({
        // language: dt_language,  // global variable defined in html
        order: [[ 0, "desc" ]],
        lengthMenu: [[25, 50, 100, 200], [25, 50, 100, 200]],
        columnDefs :columndef,
        // columnDefs: [
   
        //     {
        //         data: 'id',
        //         targets: [0],
                
 
        //     },
        //     {
        //         data: 'first_name',
        //         targets: [1]
        //     },
        //     {
        //         data: 'email',
        //         targets: [2]
        //     },
        //     {
        //         data: 'last_name',
        //         targets: [3]
        //     }
        // ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: TESTMODEL_LIST_JSON_URL,

        // "rowCallback": function( row, data ) {
        //     if ( $.inArray(data.DT_RowId, selected) !== -1 ) {
        //         $(row).addClass('selected');
        //     }
        // },


    });

    $('.datatable').DataTable().column(0).visible(false);
   
    var selectid;
    
    $('#comment-form-table tbody').on('click', 'tr', function () {
        var id = this.id;
        var index = $.inArray(id, selected);
 
        if ( index === -1 ) {
            selected.push( id );
            console.log(id,"if")
        } else {
            selected.splice( index, 1 );
            console.log(id,"if", index)
        }


        // var ada= dt_table.rows( { selected: true } ).count();


        // console.log(ada,"jumlah")
        var oData = dt_table.fnGetData(this);
      
        selectid= oData[0]
        console.log(oData.ID, oData,"ll",oData[0]);
        console.log(selected, selectid,"luasan", delete_url, edit_url)
        var editUrl= edit_url.split('/')
        var deleteUrl= delete_url.split('/')
        console.log(editUrl,"editUrl1")
        editUrl[editUrl.length - 2] = selectid
        deleteUrl[deleteUrl.length - 2] = selectid
        console.log(editUrl,"editUrl2")
        editUrl= editUrl.join('/')
        deleteUrl= deleteUrl.join('/')
        console.log(editUrl,"editUrl3")
        console.log(deleteUrl,"editUrl3")

        $('#delete-form').attr("action", deleteUrl);
        $('#delete-form').attr("method", "POST");
 

        $('#editbutton a').attr("href", editUrl);

        console.log(this)
        console.log($(this).parent())
        console.log($(this).siblings())
        $(this).siblings().removeClass('selected');
        $(this).toggleClass('selected');
        // $(this).toggleClass('selected').siblings().removeAttr('selected');
    } );

    $('#editbutton').click(function(){  
        var table = $('.datatable').DataTable();
        console.log( 'Rows '+table.rows( '.selected' ).count()+' are selected' );
        if (!table.rows( '.selected' ).count()){
            let text = "please select row";
            $('#editbutton a').attr("href", "#");
            alert(text);

            return false;
        }
    });


    $('.delete').click(function(){  
        var table = $('.datatable').DataTable();
        console.log( 'Rows '+table.rows( '.selected' ).count()+' are selected' );
        if (!table.rows( '.selected' ).count()){
            let text = "please select row";
            alert(text);
            return false;
        }

        if ( !selectid){
            let text = "please select row";
            alert(text);
            return false;
        }
        let text = "Press a button!\nEither OK or Cancel.";
      

        if (confirm(text) == true) {
          text = "You pressed OK!";
          
          return true
        } else {
          text = "You canceled!"
          return false
        }
       // Submit the form
    });
    // var table = $('.datatable').DataTable();
    // $('.datatable').on( 'click', 'tr', function () {
    //     var id = table.row(this).id();
    //     var ada= table.rows( { selected: true } ).count();
    //     console.log(ada,"koko");
    //     console.log( 'Clicked row id ' + id , table);
    //     console.log( 'Clicked row id ' + id , table.row(this));
        
    //     console.log( "lolo", table.rows('.selected').data() +' row(s) selected' );
    //   });


});