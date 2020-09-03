import py4j.GatewayServer;
import com.amazon.randomcutforest.RandomCutForest;

class AwsRcfApplication {

    public double[][] rcf(double[][] m, int numTrees, int sampleSize){
        RandomCutForest forest = RandomCutForest.builder()
            .dimensions(m[0].length)
            .numberOfTrees(numTrees)
            .sampleSize(sampleSize)
            .build();
        double[][] res = new double[m.length][m[0].length+1];
        for (int i=0; i<m.length; i++){
            double score = forest.getAnomalyScore(m[i]);
            System.arraycopy(m[i], 0, res[i], 0, m[i].length);
            res[i][res[i].length-1] = score;
            forest.update(m[i]);
        }
        return res;
    }

    public static void main(String[] args){
        System.out.println("Starting Random Cut Forest Python Binding Service");
        AwsRcfApplication app = new AwsRcfApplication();
        GatewayServer server = new GatewayServer(app);
        server.start();
    }
}
