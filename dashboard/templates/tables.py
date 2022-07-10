from app import db

filename = 'tables.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)

bot_users = []
tbl = "<tr><td>Name</td><td>Email ID</td><td>Gender</td><td>Address</td><td>Contact No</td></tr>"
bot_users.append(tbl)

for y in db.gvpbot.find():
    a = "<tr><td>%s</td>"%y['fname']+" "+['lname']
    bot_users.append(a)
    b = "<td>%s</td>"%y['Email_ID']
    bot_users.append(b)
    c = "<td>%s</td></tr>"%y['Gender']
    bot_users.append(c)
    d = "<td>%s</td></tr>"%y['Address']
    bot_users.append(d)
    f = "<td>%s</td></tr>"%y['Mobile_No']
    bot_users.append(f)

{% include 'admin-layout.html' %}

        <!-- Begin Page Content -->
        <div class="container-fluid">

          <!-- Page Heading -->
          <h1 class="h3 mb-2 text-gray-800">Bot User Information</h1>
          
          <!-- DataTales Example -->
          <div class="card shadow mb-4">
            <div class="card-body">
              <div class="table-responsive">
                <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                #   <thead>
                #     <tr>
                #       <th>Name</th>
                #       <th>Email ID</th>
                #       <th>Gender</th>
                #       <th>Address</th>
                #       <th>Contact No</th>
                #     </tr>
                #   </thead>
                #   <tfoot>
                #     <tr>
                #       <th>Name</th>
                #       <th>Email ID</th>
                #       <th>Gender</th>
                #       <th>Address</th>
                #       <th>Contact No</th>
                #     </tr>
                #   </tfoot>
                #   <tbody>
                #     <tr>
                #       <td>{{session ['user']['name'] }}</td>
                #       <td>System Architect</td>
                #       <td>Edinburgh</td>
                #       <td>2011/04/25</td>
                #       <td>$320,800</td>
                #     </tr>
                #     <tr>
                #       <td>Garrett Winters</td>
                #       <td>Accountant</td>
                #       <td>Tokyo</td>
                #       <td>2011/07/25</td>
                #       <td>$170,750</td>
                #     </tr>
                #     <tr>
                #       <td>Ashton Cox</td>
                #       <td>Junior Technical Author</td>
                #       <td>San Francisco</td>
                #       <td>2009/01/12</td>
                #       <td>$86,000</td>
                #     </tr>
                #   </tbody>
                %s
                </table>
              </div>
            </div>
          </div>

        </div>
        <!-- /.container-fluid -->

      </div>
      <!-- End of Main Content -->

      <!-- Footer -->
      <footer class="sticky-footer bg-white">
        <div class="container my-auto">
          <div class="copyright text-center my-auto">
            <span>Copyright &copy; Gujarat Vidyapith 2022</span>
          </div>
        </div>
      </footer>
      <!-- End of Footer -->

    </div>
    <!-- End of Content Wrapper -->

  </div>
  <!-- End of Page Wrapper -->

  <!-- Scroll to Top Button-->
  <a class="scroll-to-top rounded" href="#page-top">
    <i class="fas fa-angle-up"></i>
  </a>

  <!-- Bootstrap core JavaScript-->
  <script src="/static/vendor/jquery/jquery.min.js"></script>
  <script src="/static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Core plugin JavaScript-->
  <script src="/static/vendor/jquery-easing/jquery.easing.min.js"></script>

  <!-- Custom scripts for all pages-->
  <script src="/static/js/sb-admin-2.min.js"></script>

  <!-- Page level plugins -->
  <script src="/static/vendor/datatables/jquery.dataTables.min.js"></script>
  <script src="/static/vendor/datatables/dataTables.bootstrap4.min.js"></script>

  <!-- Page level custom scripts -->
  <script src="/static/js/demo/datatables-demo.js"></script>

</body>

</html>
'''%(bot_users)
print(bot_users)