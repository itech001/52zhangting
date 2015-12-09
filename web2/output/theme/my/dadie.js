
  $(document).ready(function() {
  $('#mytable3').dataTable( {
    searching: true,
    paging: true,
    ordering: true,
    orderMulti : true,
    pageLength: 100,
    order: [[ 2, 'desc' ],[ 7, 'desc' ]],
    columnDefs: [
    {
      targets: [ 2 ],
      orderData: [ 2, 7 ]
    },
    {
      targets: [ 7],
      orderData: [ 7, 2 ]
    },
    {
      targets: [ 3],
      orderData: [ 3, 6 ]
    },
    {
      targets: [ 5],
      orderData: [ 5, 7 ]
    },
    {
      targets: [ 4],
      orderData: [ 4, 7 ]
    },
    {
      targets: [ 6],
      orderData: [ 6, 7 ]
    }   ],
     columns: [    { type: "html" },    { type: "html" },    { type: "num" },    { type: "num" },{ type: "num" }, {type:"num"} ,{type:"num"} , {type:"num"},{ type: "html" }]
  } );
} );
