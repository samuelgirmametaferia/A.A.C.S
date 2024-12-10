import org.libGDX.core.ApplicationAdapter;
import org.libGDX.core.Gdx;
import org.libGDX.graphics.OrthographicCamera;
import org.libGDX.graphics.SpriteBatch;
import org.libGDX.input.InputProcessor;
import org.libGDX.math.Vector2;

public class CitySimulator extends ApplicationAdapter implements InputProcessor {

    private OrthographicCamera camera;
    private SpriteBatch batch;

    @Override
    public void create() {
        camera = new OrthographicCamera();
        batch = new SpriteBatch();
        Gdx.input.setInputProcessor(this);
    }

    @Override
    public void render() {
        Gdx.gl.glClearColor(0, 0, 0, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        camera.update();
        batch.setProjectionMatrix(camera.combined);

        batch.begin();
        // Draw city elements
        batch.end();
    }

    @Override
    public boolean keyDown(int keycode) {
        return false;
    }

    @Override
    public boolean keyUp(int keycode) {
        return false;
    }

    @Override
    public boolean keyTyped(char character) {
        return false;
    }

    @Override
    public boolean touchDown(int screenX, int screenY, int pointer, int button) {
        return false;
    }

    @Override
    public boolean touchUp(int screenX, int screenY, int pointer, int button) {
        return false;
    }

    @Override
    public boolean touchDragged(int screenX, int screenY, int pointer) {
        return false;
    }

    @Override
    public boolean mouseMoved(int screenX, int screenY) {
        return false;
    }

    @Override
    public boolean scrolled(int amount) {
        return false;
    }
}