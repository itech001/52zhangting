
  $(document).ready(function() {
  $('#mytable3').dataTable( {
    searching: true,
    paging: true,
    ordering: true,
    orderMulti : true,
    pageLength: 100,
    order: [[ 2, 'desc' ],[ 6, 'desc' ],
    columnDefs: [
    {
      targets: [ 2 ],
      orderData: [ 2, 6 ]
    },
    {
      targets: [ 6],
      orderData: [ 6, 2 ]
    },
    {
      targets: [ 3],
      orderData: [ 3, 6 ]
    },
    {
      targets: [ 2],
      orderData: [ 2, 4, 8 ]
    },
    {
      targets: [ 4],
      orderData: [ 4, 6 ]
    },
    {
      targets: [ 5],
      orderData: [ 5, 6 ]
    }   ],
     columns: [    { type: "html" },    { type: "html" },    { type: "num" },    { type: "num" }, {type:"num"} ,{type:"num"} , {type:"num"},{ type: "html" }]
  } );
} );
